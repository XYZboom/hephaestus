from src.analysis import type_dependency_analysis as tda
from src.ir import ast, types as tp, kotlin_types as kt, context as ctx
from tests.resources import type_analysis_programs as tap



def assert_nodes(nodes, expected_nodes):
    assert set(nodes) == set(expected_nodes)


def tuple2str(tpl):
    return "/".join(tpl)


def to_str_dict(res):
    new_res = {}
    for k, v in res.items():
        new_res[str(k)] = [str(i) for i in v]
    return new_res


def test_program1():
    # Foo<String> x = new Foo<String>()
    program = tap.program1
    a = tda.TypeDependencyAnalysis(program, kt.KotlinBuiltinFactory())
    a.visit(program)
    res = to_str_dict(a.result())
    assert res == {
        '!TypeVariable[global/x/Foo/T]': [
            "-> TypeVariable[global/x/Foo/T] (inferred)",
            "-> Type[String] (declared)"
        ],
        "Declaration[global/x]": [
            "-> TypeConInstCall[global/x/Foo] (inferred)",
            "-> TypeConInstDecl[global/x/Foo] (declared)"
        ],
        'TypeConInstCall[global/x/Foo]': [
            '-> TypeVariable[global/x/Foo/T] (declared)'
        ],
        'TypeConInstDecl[global/x/Foo]': [
            '-> !TypeVariable[global/x/Foo/T] (declared)'
        ],
        'TypeVariable[global/x/Foo/T]': ['-> Type[String] (declared)']
    }


def test_program2():
    # String x = "f"
    # Foo<String> y = new Foo<String>(x)
    program = tap.program2
    a = tda.TypeDependencyAnalysis(program, kt.KotlinBuiltinFactory())
    a.visit(program)
    res = to_str_dict(a.result())

    assert res == {
        '!TypeVariable[global/y/Foo/T]': [
            '-> TypeVariable[global/y/Foo/T] (inferred)',
            '-> Type[String] (declared)'
        ],
        'Declaration[global/Foo/f]': ['-> Type[T] (declared)'],
        'Declaration[global/x]': [
            '-> Type[String] (inferred)',
            '-> Type[String] (declared)',
        ],
        'Declaration[global/y]': [
            '-> TypeConInstCall[global/y/Foo] (inferred)',
            '-> TypeConInstDecl[global/y/Foo] (declared)'
        ],
        'TypeConInstCall[global/y/Foo]': [
            '-> TypeVariable[global/y/Foo/T] (declared)'
        ],
        'TypeConInstDecl[global/y/Foo]': [
            '-> !TypeVariable[global/y/Foo/T] (declared)'
        ],
        'TypeVariable[global/y/Foo/T]': [
            '-> Type[String] (declared)',
            '-> Declaration[global/x] (inferred)'
        ]
    }



def test_program3():
    # String x ="f"
    # Bar y = new Bar(new Foo<String>(x))
    program = tap.program3
    a = tda.TypeDependencyAnalysis(program, kt.KotlinBuiltinFactory())
    a.visit(program)
    res = to_str_dict(a.result())

    assert res == {
        '!TypeVariable[global/Bar/f/Foo/T]': [
            '-> TypeVariable[global/Bar/f/Foo/T] (inferred)',
            '-> Type[String] (declared)'
        ],
        'Declaration[global/Bar/f]': ['-> Type[Foo] (declared)'],
        'Declaration[global/Foo/f]': ['-> Type[T] (declared)'],
        'Declaration[global/x]': [
            '-> Type[String] (inferred)',
            '-> Type[String] (declared)'
        ],
        'Declaration[global/y]': [
            '-> Type[Bar] (inferred)',
            '-> Type[Bar] (declared)'
        ],
        'TypeConInstCall[global/Bar/f/Foo]': [
            '-> TypeVariable[global/Bar/f/Foo/T] (declared)'
        ],
        'TypeConInstDecl[global/Bar/f/Foo]': [
            '-> !TypeVariable[global/Bar/f/Foo/T] (declared)'
        ],
        'TypeVariable[global/Bar/f/Foo/T]': [
            '-> Type[String] (declared)',
            '-> Declaration[global/x] (inferred)'
        ]

    }


def test_program4():
    # class A<T>
    # class B<T, T2> : A<T2>()
    # class C<T> : B<String, T>()
    # val x: A<String> = new C<String>()

    program = tap.program4
    a = tda.TypeDependencyAnalysis(program, kt.KotlinBuiltinFactory())
    a.visit(program)
    res = to_str_dict(a.result())

    assert res == {
        '!TypeVariable[global/x/A/T]': [
            '-> TypeVariable[global/x/C/T] (inferred)',
            '-> Type[String] (declared)'
        ],
        'Declaration[global/x]': [
            '-> TypeConInstCall[global/x/C] (inferred)',
            '-> TypeConInstDecl[global/x/A] (declared)'
        ],
        'TypeConInstCall[global/x/C]': [
            '-> TypeVariable[global/x/C/T] (declared)'
        ],
        'TypeConInstDecl[global/x/A]': [
            '-> !TypeVariable[global/x/A/T] (declared)'
        ],
        'TypeVariable[global/x/C/T]': ['-> Type[String] (declared)']
    }
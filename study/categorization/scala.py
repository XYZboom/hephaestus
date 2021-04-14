from bug import ScalaBug
import categories as ct
import characteristics as pc
import symptoms as sy
import root_causes as rc


scala_iter1 = [
    ScalaBug(
        "1.Scala2-8675",
        [pc.Arrays(), pc.Loops()],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.ErrorReporting(),
        9
    ),
    ScalaBug(
        "2.Scala2-11843",
        [pc.Cast()],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Environment(),
        1
    ),
    ScalaBug(
        "3.Dotty-5636",
        [pc.ParameterizedClasses(),
         pc.ParameterizedTypes(),
         pc.DependentTypes(),
         pc.Inheritance()
         ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        7
    ),
    ScalaBug(
        "4.Dotty-8802",
        [
         pc.DependentTypes(),
         pc.ParameterizedTypes(),
         pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.TypeArgsInference(),
         pc.Implicits(),
         pc.Typedefs(),
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Inference(),
        11
    ),
    ScalaBug(
        "5.Dotty-4509",
        [
         pc.Implicits(),
         pc.FunctionTypes(),
         pc.ErasedParameters(),
         pc.Lambdas()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Transformation(),
        4
    ),
    ScalaBug(
        "6.Scala2-5878",
        [
         pc.ValueClasses(),
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        2
    ),
    ScalaBug(
        "7.Scala2-5886",
        [
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.Reflection(),
            pc.CallByName(),
            pc.FunctionReferences(),
            pc.FunctionTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.IncorrectAnalysisMechanics(),
        8
    ),
    ScalaBug(
        "8.Scala2-7928",
        [
            pc.Inheritance(), pc.NestedClasses(),
            pc.Collections(), pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.Overriding(), pc.DependentTypes(), pc.Typedefs(),
            pc.Subtyping()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.Transformation(),
        13
    ),
    ScalaBug(
        "9.Dotty-1757",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.DefaultInitializer()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Inference(),  # type variable substitution
        4
    ),
    ScalaBug(
        "10.Dotty-6146",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.FBounded(),
            pc.WildCardType(),
            pc.Inheritance(),
            pc.SealedClasses(),
            pc.Singleton(),
            pc.Implicits()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectSequence(),
        ct.TypeComparison(),
        9
    ),
    ScalaBug(
        "11.Scala2-9542",
        [pc.ValueClasses(), pc.NestedClasses(),
         pc.ParameterizedClasses(), pc.ParameterizedTypes()],
        True,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.Transformation(),
        24
    ),
    ScalaBug(
        "12.Dotty-2234",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.Overloading(),
            pc.Typedefs()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        3
    ),
    ScalaBug(
        "13.Scala2-9361",
        [
            pc.HigherKindedTypes(),
            pc.WildCardType(),
            pc.Overriding(),
            pc.Subtyping(),
            pc.Nothing(),
            pc.Typedefs(),
            pc.TypeArgsInference()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.ErrorReporting(),
        5
    ),
    ScalaBug(
        "14.Scala2-4098",
        [
            pc.This()
        ],
        False,
        sy.Runtime(sy.VerifyError()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        6
    ),
    ScalaBug(
        "15.Dotty-10325",
        [
            pc.ParameterizedFunctions(),
            pc.OptionTypes(),
            pc.Collections(),
            pc.Overloading(),
            pc.TypeArgsInference(),
            pc.FunctionReferences(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.IncorrectAnalysisMechanics(),
        7
    ),
    ScalaBug(
        "16.Dotty-9044",
        [
            pc.ParameterizedClasses(), pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(), pc.HigherKindedTypes(),
            pc.DeclVariance(), pc.AlgebraicDataTypes(),
            pc.CaseClasses(), pc.Inheritance(),
            pc.MultipleImplements(), pc.FunctionTypes(),
            pc.Subtyping(), pc.Implicits(), pc.PatMat()
        ],
        False,
        sy.MisleadingReport(),
        rc.DesignIssue(),
        ct.Inference(),
        9
    ),
    ScalaBug(
        "17.Dotty-4470",
        [
            pc.Enums()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Transformation(),
        6
    ),
    ScalaBug(
        "18.Dotty-8752",
        [
            pc.TypeLambdas(), pc.ParameterizedClasses(),
            pc.FBounded(), pc.ParameterizedTypes(),
            pc.Collections()
        ],
        False,
        sy.MisleadingReport(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        2
    ),
    ScalaBug(
        "19.Scala2-10185",
        [
            pc.ParameterizedTypes(), pc.ParameterizedClasses(),
            pc.BoundedPolymorphism(), pc.HigherKindedTypes(),
            pc.AlgebraicDataTypes(), pc.PatMat(),
            pc.Inheritance(), pc.CaseClasses()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.TypeComparison(),
        8
    ),
    ScalaBug(
        "20.Dotty-5188",
        [
            pc.Inline(), pc.Varargs()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        4
    )

]


scala_iter2 = [
    ScalaBug(
        "1.Scala2-8763",
        [
            pc.Collections(), pc.PatMat(),
            pc.Arrays(),
            pc.VarTypeInference(),
            pc.AugmentedAssignmentOperator()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        4
    ),
    ScalaBug(
        "2.Scala2-5231",
        [
            pc.AccessModifiers(), pc.Implicits()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.IncorrectAnalysisMechanics(),
        6
    ),
    ScalaBug(
        "3.Scala2-11239",
        [
            pc.ParameterizedClasses(), pc.Typedefs(),
            pc.HigherKindedTypes(), pc.CaseClasses(),
            pc.BoundedPolymorphism(), pc.ParameterizedTypes(),
            pc.TypeProjections()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        4
    ),
    ScalaBug(
        "4.Dotty-9735",
        [
            pc.Typedefs(), pc.TypeLambdas(),
            pc.ParameterizedClasses(),
            pc.OpaqueType(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.MisleadingReport(),
        rc.IncorrectCondition(),
        ct.MissingValiationChecks(),
        3
    ),
    ScalaBug(
        "5.Scala2-10886",
        [
            pc.Import(),
            pc.AugmentedAssignmentOperator(),
            pc.ArithmeticExpressions()
        ],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.IncorrectAnalysisMechanics(),
        9
    ),
    ScalaBug(
        "6.Dotty-9803",
        [
            pc.Overloading(), pc.Import()
        ],
        False,
        sy.MisleadingReport(),
        rc.WrongParams(),
        ct.Resolution(),
        11
    ),
    ScalaBug(
        "7.Dotty-5140",
        [
            pc.JavaInterop(), pc.Arrays(),
            pc.Varargs(),
            pc.Inheritance(), pc.Subtyping()
        ],
        True,
        sy.InternalCompilerError(),
        rc.DesignIssue(),
        ct.Approximation(),
        10
    ),
    ScalaBug(
        "8.Dotty-4487",
        [
            pc.Inheritance(), pc.FunctionTypes(),
            pc.CallByName()
        ],
        False,
        sy.InternalCompilerError(),
        rc.DesignIssue(),
        ct.IncorrectAnalysisMechanics(),
        1
    ),
    ScalaBug(
        "9.Dotty-3585",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.This(),
            pc.OptionTypes(),
            pc.CallByName(),
            pc.Implicits(),
        ],
        True,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.Resolution(),
        13
    ),
    ScalaBug(
        "10.Dotty-9631",
        [
            pc.AccessModifiers(),
            pc.Singleton(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
            pc.FBounded(),
            pc.NestedClasses(),
            pc.Inheritance(),
            pc.AlgebraicDataTypes(),
            pc.SelfTypes(),
            pc.Implicits(),
            pc.WildCardType(),
            pc.PatMat()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.TypeComparison(),
        15
    ),
    ScalaBug(
        "11.Dotty-10217",
        [
            pc.UnionTypes(), pc.ParameterizedClasses(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompilationPerformance(),
        rc.AlgorithmImproperlyImplemented(),
        ct.TypeComparison(),
        27
    ),
    ScalaBug(
        # regression bug
        "12.Scala2-7482",
        [
            pc.JavaInterop(), pc.Collections(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Approximation(),
        2
    ),
    ScalaBug(
        "13.Scala2-5454",
        [
            pc.Implicits(),
            pc.Inheritance(), pc.ParameterizedClasses()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Environment(),
        7
    ),
    ScalaBug(
        "14.Scala2-6714",
        [
            pc.Overriding(), pc.Implicits(),
            pc.ArithmeticExpressions(),
            pc.SpecialMethodOverriding(),
            pc.AugmentedAssignmentOperator()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Transformation(),
        10
    ),
    ScalaBug(
        "15.Dotty-3917",
        [
            pc.Inheritance()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Transformation(),
        8
    ),
    ScalaBug(
        "16.Dotty-2723",
        [
            pc.Inline(), pc.Implicits(), pc.FunctionTypes()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectDataType(),
        ct.Transformation(),
        3
    ),
    ScalaBug(
        "17.Dotty-4030",
        [
            pc.Inheritance(), pc.AlgebraicDataTypes(),
            pc.CaseClasses(), pc.Singleton(),
            pc.ParameterizedFunctions(), pc.TypeArgsInference(),
            pc.ParameterizedClasses(), pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(), pc.FunctionTypes(),
            pc.UnionTypes(), pc.WildCardType()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.IncorrectAnalysisMechanics(),
        11
    ),
    ScalaBug(
        "18.Scala2-10536",
        [
            pc.ParameterizedClasses(), pc.Implicits(),
            pc.FBounded(), pc.BoundedPolymorphism(),
            pc.AlgebraicDataTypes(), pc.Overloading(),
            pc.Inheritance(), pc.CaseClasses(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        6
    ),
    ScalaBug(
        "19.Dotty-9749",
        [
            pc.Varargs()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        6
    ),
    ScalaBug(
        "20.Dotty-3422",
        [
            pc.HigherKindedTypes(), pc.NestedClasses(),
            pc.ParameterizedClasses(),
            pc.DependentTypes(), pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        7
    )
]

scala_iter3 = [
    ScalaBug(
        "1.Dotty-10123",
        [
            pc.ParameterizedClasses(),
            pc.NestedClasses(),
            pc.TypeArgsInference(),
            pc.DeclVariance(),
            pc.Implicits(),
            pc.ParameterizedTypes(),
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        19
    ),
    ScalaBug(
        # regression bug
        "2.Scala2-5399",
        [
            pc.ParameterizedClasses(),
            pc.NestedClasses(),
            pc.ParameterizedTypes(),
            pc.Inheritance(),
            pc.AlgebraicDataTypes(),
            pc.CaseClasses(),
            pc.WildCardType(),
            pc.PatMat()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        19
    ),
    ScalaBug(
        "3.Dotty-7597",
        [
            pc.ParameterizedFunctions(),
            pc.BoundedPolymorphism(),
            pc.TypeArgsInference(),
            pc.SpecialMethodOverriding(),
            pc.AnonymousClass()
        ],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.InsufficientAlgorithmImplementation(),
        ct.MissingValiationChecks(),
        2
    ),
    ScalaBug(
        "4.Scala2-5958",
        [
            pc.This(),
            pc.SelfTypes(),
            pc.FunctionReferences(),
            pc.DependentTypes(),
            pc.NestedClasses()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        12
    ),
    ScalaBug(
        "5.Scala2-7872",
        [
            pc.TypeProjections(),
            pc.HigherKindedTypes(),
            pc.Collections(),
            pc.ETAExpansion(),
            pc.Typedefs(),
            pc.FunctionTypes(),
            pc.Subtyping(),
            pc.DeclVariance(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.MissingValiationChecks(),
        13
    ),
    ScalaBug(
        "6.Scala2-2038",
        [
            pc.Collections(),
            pc.WildCardType(),
            pc.Reflection(),
            pc.PatMat(),
            pc.TypeArgsInference(),
            pc.SpecialMethodOverriding(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.Approximation(),
        5
    ),
    ScalaBug(
        "7.Scala2-5378",
        [
            pc.ParameterizedClasses(),
            pc.SpecialMethodOverriding(),
            pc.Collections(),
            pc.DeclVariance(),
            pc.AnonymousClass(),
            pc.VarTypeInference(),
            pc.ParameterizedFunctions(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.Runtime(sy.MissingMethodException()),
        rc.IncorrectComputation(),
        ct.MissingValiationChecks(),
        12
    ),
    ScalaBug(
        "8.Scala2-5687",
        [
            pc.ParameterizedClasses(),
            pc.AccessModifiers(),
            pc.BoundedPolymorphism(),
            pc.Typedefs(),
            pc.Cast(),
            pc.This(),
            pc.ParameterizedTypes(),
            pc.Inheritance(),
            pc.Overriding()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        18
    ),
    ScalaBug(
        "9.Scala2-11252",
        [
            pc.PatMat(),
            pc.SpecialMethodOverriding(),
            pc.ParameterizedTypes(),
            pc.Conditionals(),
            pc.OptionTypes(),
            pc.CaseClasses(),
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        13
    ),
    ScalaBug(
        "10.Scala2-8344",
        [
            pc.Overloading(),
            pc.Varargs()
        ],
        False,
        sy.Runtime(sy.WrongResult()),
        rc.DesignIssue(),
        ct.Resolution(),
        5
    ),
    ScalaBug(
        "11.Scala2-2509",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.DeclVariance(),
            pc.Inheritance(),
            pc.Singleton(),
            pc.Overriding(),
            pc.Subtyping(),
            pc.Implicits(),
        ],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.DesignIssue(),
        ct.Resolution(),
        28
    ),
    ScalaBug(
        "12.Scala2-4775",
        [
            pc.Overloading(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.Varargs(),
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.Resolution(),
        29
    ),
    ScalaBug(
        "13.Scala2-8862",
        [
            pc.Implicits(),
            pc.Import(),
            pc.ParameterizedTypes(),
            pc.OptionTypes(),
            pc.Inheritance(),
            pc.Overriding(),
            pc.ParameterizedClasses()
        ],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Environment(),
        25
    ),
    ScalaBug(
        "14.Scala2-9231",
        [
            pc.ParameterizedClasses(),
            pc.Implicits(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
        ],
        False,
        sy.MisleadingReport(),
        rc.IncorrectCondition(),
        ct.Resolution(),
        9
    ),
    ScalaBug(
        "15.Dotty-7041",
        [
            pc.Inline(),
            pc.CallByName(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedFunctions(),
            pc.WildCardType(),
            pc.TypeArgsInference(),
            pc.TryCatch(),
            pc.Conditionals(),
            pc.FunctionAPI(),
            pc.Lambdas(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectComputation(),
        ct.Approximation(),
        13
    ),
    ScalaBug(
        "16.Dotty-4754",
        [
            pc.Import(),
            pc.AccessModifiers(),
            pc.Singleton(),
            pc.Inline()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.Transformation(),
        13
    ),
    ScalaBug(
        "17.Scala2-4691",
        [
            pc.Inheritance(),
            pc.PatMat(),
            pc.AlgebraicDataTypes(),
            pc.Inheritance(),
            pc.OptionTypes(),
            pc.SpecialMethodOverriding(),
            pc.ParameterizedTypes(),
        ],
        False,
        sy.Runtime(sy.CaseNotFound()),
        rc.DesignIssue(),
        ct.MissingValiationChecks(),
        18
    ),
    ScalaBug(
        "18.Dotty-6451",
        [
            pc.TypeLambdas(),
            pc.Typedefs(),
            pc.HigherKindedTypes(),
            pc.Collections(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        2
    ),
    ScalaBug(
        "19.Scala2-9760",
        [
            pc.HigherKindedTypes(),
            pc.AlgebraicDataTypes(),
            pc.CaseClasses(),
            pc.ParameterizedTypes(),
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.TypeArgsInference(),
            pc.Inheritance(),
            pc.PatMat(),
            pc.Collections()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.Inference(),
        18
    ),
    ScalaBug(
        "20.Scala2-10186",
        [
            pc.HigherKindedTypes(),
            pc.BoundedPolymorphism(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
            pc.Typedefs()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        12
    )
]

scala_iter4 = [
    ScalaBug(
        "1.Dotty-5876",
        [
            pc.Inheritance(),
            pc.MultiBounds(),
            pc.Typedefs(),
            pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.Overriding()
        ],
        True,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),
        ct.TypeComparison(),
        9
    ),
    ScalaBug(
        "2.Scala2-2742",
        # pc.VarTypeInference() val f = new A
        [
            pc.Implicits(),
            pc.Inheritance(),
            pc.Overriding(),
            pc.VarTypeInference(),
            pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.DesignIssue(),
        ct.MissingValiationChecks(),
        12
    ),
    ScalaBug(
        "3.Dotty-2192",
        [
            pc.ParameterizedTypes(),
            pc.PatMat(),
            pc.Subtyping()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        5
    ),
    ScalaBug(
        "4.Scala2-9630",
        [
            pc.AlgebraicDataTypes(),
            pc.Inheritance(),
            pc.CaseClasses(),
            pc.PatMat(),
        ],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.IncorrectAnalysisMechanics(),
        12
    ),
    ScalaBug(
        "5.Dotty-6745",
        [
            pc.DependentTypes(),
            pc.SelfTypes(),
            pc.Typedefs(),
            pc.This(),
            pc.FunctionTypes(),
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        4
    ),
    ScalaBug(
        "6.Dotty-2219",
        [
            pc.ParameterizedClasses(),
            pc.ParameterizedTypes(),
            pc.BoundedPolymorphism(),
            pc.HigherKindedTypes(),
            pc.FunctionTypes(),
            pc.WildCardType(),
            pc.Typedefs()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        0
    ),
    ScalaBug(
        "7.Scala2-6754",
        [
            pc.ParameterizedClasses(),
            pc.BoundedPolymorphism(),
            pc.Reflection(),
            pc.Collections(),
            pc.PatMat()
        ],
        True,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        0
    ),
    ScalaBug(
        "8.Scala2-7232",
        [
            pc.JavaInterop(),
        ],
        True,
        sy.Runtime(sy.ClassCastException()),
        rc.FunctionalSpecificationMismatch(),
        ct.Resolution(),
        0
    ),
    ScalaBug(
        # pc.regression bug
        "9.Scala2-7688",
        [
            pc.ParameterizedClasses(),
            pc.Singleton(),
            pc.BoundedPolymorphism(),
            pc.TypeProjections(),
            pc.Mixins(),
            pc.SpecialMethodOverriding(),
            pc.Reflection(),
            pc.ParameterizedTypes(),
            pc.DependentTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Approximation(),
        0
    ),
    ScalaBug(
        # regression bug
        "10.Scala2-9086",
        [
            pc.ParameterizedClasses(),
            pc.Singleton(),
            pc.ParameterizedTypes(),
            pc.Inheritance(),
            pc.TypeArgsInference(),
            pc.Implicits()
        ],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Environment(),
        0
    ),
    ScalaBug(
        "11.Dotty-8647",
        [
            pc.ParameterizedClasses(),
            pc.WildCardType(),
            pc.Typedefs(),
            pc.MatchTypes(),
            pc.PatMat(),
            pc.ParameterizedTypes()
        ],
        True,
        sy.CompileTimeError(),
        rc.ExtraneousComputation(),
        ct.TypeComparison(),
        0
    ),
    ScalaBug(
        # regression bug
        "12.Scala2-8531",
        [
            pc.Enums(),
            pc.PatMat(),
            pc.JavaInterop()
        ],
        True,
        sy.CompilationPerformance(),
        rc.InsufficientAlgorithmImplementation(),
        ct.MissingValiationChecks(),
        0
    ),
    ScalaBug(
        "13.Scala2-6912",
        [
            pc.ParameterizedFunctions(),
            pc.SpecialMethodOverriding(),
            pc.NamedArgs(),
            pc.Overloading(),
            pc.Nothing(),
            pc.ParameterizedTypes()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        0
    ),
    ScalaBug(
        "14.Dotty-2104",
        [
            pc.CaseClasses(),
            pc.Singleton(),
            pc.SpecialMethodOverriding(),
            pc.ParameterizedClasses(),
            pc.ParameterizedFunctions(),
            pc.ParameterizedTypes(),
            pc.DeclVariance(),
            pc.Overriding(),
            pc.PatMat()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),
        0
    ),
    ScalaBug(
        "15.Dotty-5640",
        [
            pc.Lambdas(),
            pc.VarTypeInference()
        ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectSequence(),
        ct.Transformation(),
        0
    ),
    ScalaBug(
        "16.Dotty-3067",
        [
            pc.ParameterizedClasses(),
            pc.ParamTypeInference(),
            pc.Lambdas(),
            pc.ETAExpansion(),
            pc.Singleton(),
            pc.Collections(),
            pc.ParameterizedTypes(),
            pc.FunctionTypes(),
            pc.Implicits(),
            pc.Inheritance()
        ],
        True,
        sy.CompileTimeError(),
        rc.InsufficientAlgorithmImplementation(),
        ct.Resolution(),
        0
    ),
    ScalaBug(
        # regression bug
        "17.Scala2-7636",
        [
            pc.ParameterizedClasses(),
            pc.WildCardType(),
            pc.ParameterizedTypes(),
            pc.Inheritance(),
            pc.Collections()
        ],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.ErrorReporting(),
        0
    ),
    ScalaBug(
        "18.Scala2-9110",
        [
            pc.NestedClasses(),
            pc.CaseClasses(),
            pc.Inheritance(),
            pc.Singleton(),
            pc.AlgebraicDataTypes(),
            pc.PatMat()
        ],
        True,
        sy.Runtime(sy.WrongResult()),
        rc.MissingCase(),
        ct.IncorrectAnalysisMechanics(),
        0
    ),
    ScalaBug(
        "19.Scala2-10545",
        [
            pc.HigherKindedTypes(),
            pc.ParameterizedClasses(),
            pc.SpecialMethodOverriding(),
            pc.ParameterizedTypes(),
            pc.ParameterizedFunctions(),
            pc.Singleton(),
            pc.Implicits()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.TypeComparison(),
        0
    ),
    ScalaBug(
        "20.Scala2-9398",
        [
            pc.AlgebraicDataTypes(),
            pc.CaseClasses(),
            pc.Inheritance(),
            pc.Singleton(),
            pc.PatMat()
        ],
        False,
        sy.Runtime(sy.CaseNotFound()),
        rc.InsufficientAlgorithmImplementation(),
        ct.MissingValiationChecks(),
        0
    ),
]

#!/usr/bin/env bash
TIME_TO_RUN=$((23 * 60 * 60))
HOUR=$((60 * 60))
CORES=$(cat /proc/cpuinfo | grep processor | wc -l)
CORES=$(($CORES - 2))
TRANSFORMATIONS=40
VERSIONS="1.4.21 1.4.20 1.4.10 1.4.0 1.3.72 1.3.71 1.3.70 1.3.61 1.3.60 1.3.50 1.3.41 1.3.40 1.3.31 1.3.30 1.3.21 1.3.20 1.3.11 1.3.10 1.3.0 1.2.71 1.2.70 1.2.61 1.2.60 1.2.51 1.2.50 1.2.41 1.2.40 1.2.31 1.2.30 1.2.21 1.2.20 1.2.10 1.2.0 1.1.61 1.1.60 1.1.51 1.1.50 1.1.4-3 1.1.4-2 1.1.4 1.1.3-2 1.1.3 1.1.2-5 1.1.2-2 1.1.2 1.1.1 1.1 1.0.7 1.0.6 1.0.5-2 1.0.5 1.0.4 1.0.3 1.0.2 1.0.1-2 1.0.1-1 1.0.1 1.0.0"


simple_run() {
    cd $CHECK_TYPE_SYSTEMS
    git pull
    python3 main.py -s $TIME_TO_RUN -t $TRANSFORMATIONS -w $CORES -l
}

run_from_source() {
    cd $KOTLIN_INSTALLATION
    ./gradlew clean git pull
    ./gradlew -Dhttp.socketTimeout=60000 -Dhttp.connectionTimeout=60000 dist
    cd $CHECK_TYPE_SYSTEMS
    git pull
    python3 main.py -s $TIME_TO_RUN -t $TRANSFORMATIONS -w $CORES -l
}

run_multiple_versions() {
    cd $CHECK_TYPE_SYSTEMS
    git pull
    for i in {1..22}; do
        length=$(echo "$VERSIONS" | wc -w)
        rnum=$((1 + $RANDOM%$length+1));
        version=$(echo $VERSIONS | cut -d " " -f $rnum)
        sdk use kotlin $version
        python3 main.py -s $HOUR -t $TRANSFORMATIONS -w $CORES -l
    done
}

if [ $# -eq 0 ]
then
        echo "Missing options!"
        echo "(run $0 -h for help)"
        echo ""
        exit 0
fi

while getopts "hrsa" OPTION; do
        case $OPTION in

                r)
                        simple_run
                        ;;

                s)
                        run_from_source
                        ;;

                a)
                        run_multiple_versions
                        ;;

                h)
                        echo "Usage:"
                        echo "run.sh -s "
                        echo "init.sh -r "
                        echo "init.sh -s "
                        echo "init.sh -a "
                        echo ""
                        echo "   -r     Simple run"
                        echo "   -s     Run from source"
                        echo "   -a     Run multiple versions"
                        echo "   -h     help (this output)"
                        exit 0
                        ;;

        esac
done
#!/bin/bash

# init if needed, init=true, default is false, use command (init=true) to init, eg: init=true ./run.sh
if [ "$init" = "true" ]; then
    echo "Initializing..."
    # create virtual environment if not exist
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python -m venv venv
    fi

    # activate virtual environment
    source venv/bin/activate
    echo "Virtual environment activated"    

    # install dependencies
    pip install -r requirements.txt
    echo "Dependencies installed"
fi


# run the script
echo "Running the script..."
# python src/demo/main.py
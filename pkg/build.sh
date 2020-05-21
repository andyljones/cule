mkdir -p build
cd build

cmake -GNinja ..
ninja -v 

$PYTHON setup.py install
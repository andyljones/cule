mkdir -p build
cd build

cmake -GNinja ..
ninja -v 
mv torchcule_atari.so ..

cd ..
$PYTHON setup.py install
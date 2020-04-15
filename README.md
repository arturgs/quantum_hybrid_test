# quantum_hybrid_test
Test of Classical-Quantum hybrid architecture: a program running on a classical device (i.e. a normal computer) with function calls performed on a Quantum device assisting the computation. As we don't provide a Quantum device, we simulate one of a small size.

The code runs a simple optimization that starts in a classical device.
Run:

`
python hybrid_optimization.py
`

Code should be self-sustained, with no external dependencies. The folders `gates` and `states`provide a minimal Quantum simulator of small size. Folder `optimizations` includes a basic optimizators based on SPSA which performs the function calls to the Quantum device, and collects the result.

The code comments inside `hybrid_optimization.py` should clarify the working of this example.

#include <Python.h>
#include "eclipy.h"

// Python wrapper for the `add` function
static PyObject* eclipy_add(PyObject *self, PyObject *args) {
      double a, b;

    // Parse Python arguments
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }

    // Call the C library function
    double result = add(a, b);

    // Return the result as a Python object
    return Py_BuildValue("d", result);
}

// Method definitions
static PyMethodDef EclipyMethods[] = {
  {"add", eclipy_add, METH_VARARGS, "Add two numbers."},
  {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef EclipyModule = {
    PyModuleDef_HEAD_INIT,
    "eclipy",              // Module name
    "", // Module docstring
    -1,                     // Size of per-interpreter state
    EclipyMethods          // Method table
};

PyMODINIT_FUNC PyInit_eclipy(void) {
   return PyModule_Create(&EclipyModule);
}

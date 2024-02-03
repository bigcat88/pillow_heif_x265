#define PY_SSIZE_T_CLEAN

#include "Python.h"
#include "third-party/libheif/plugins/encoder_x265.cc"

/* =========== Module =========== */

static int setup_module(PyObject* m) {
    return 0;
}

PyMODINIT_FUNC PyInit__x265(void) {
    static PyModuleDef module_def = {
        PyModuleDef_HEAD_INIT,
        "_x265", /* m_name */
        NULL,   /* m_doc */
        -1,     /* m_size */
        NULL,   /* m_methods */
    };

    PyObject* m = PyModule_Create(&module_def);
    if (setup_module(m) < 0)
        return NULL;
    return m;
}

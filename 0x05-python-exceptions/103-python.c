#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - func to gives data of the PYfloatObject.
 * @p: the PyObject.
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *stri = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	stri = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", stri);
}
/**
 * print_python_bytes - func to gives data of  PyBytesObject.
 * @p: the PyObject.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, z = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (z < size + 1 && z < 10)
	{
		printf(" %02hhx", string[z]);
		z++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int z = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (z < size)
		{
			item = PyList_GET_ITEM(p, z);
			printf("Element %d: %s\n", z, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			z++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

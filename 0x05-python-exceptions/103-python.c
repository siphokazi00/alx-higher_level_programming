#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list
 * @p: Pointer to a Python object (list)
 *
 * Description: This function prints information about a Python list,
 * including its size and allocated space, and the types of its elements.
 * If an element is a bytes object, it calls print_python_bytes to print
 * additional information.
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (strcmp(Py_TYPE(list->ob_item[i])->tp_name, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to a Python object (bytes)
 *
 * Description: This function prints information about a Python bytes object,
 * including its size, the first 10 bytes in hexadecimal format, and the
 * corresponding string representation.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to a Python object (float)
 *
 * Description: This function prints information about a Python float object,
 * including its value.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %lf\n", value);
}

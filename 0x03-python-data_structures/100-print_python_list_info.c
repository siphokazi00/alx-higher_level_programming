#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print information about a Python list.
 * @p: Pointer to a Python object (list).
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, alloc, i;
	PyObject *item;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

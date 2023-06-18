#include "python.h"

void print_python_list_info(PyObject *p)
{
PyListObject *cast;
Py_ssize_t i, list_size;
PyObject *item;
char *type_item;

list_size = PyList_Size(p);
cast = (PyListObject *) p;
printf("[*] Size of the Python List = %d\n", (int)list_size);
printf("[*] Allocated = %d\n", (int)cast->allocated);

for (i = 0; i < list_size; i++)
{
item = PyList_GetItem(p, i);
type_item = Py_TYPE(item)->tp_name;

printf("Element %d: %s\n", (int)i, type_item);
}
}

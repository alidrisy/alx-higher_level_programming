#include <stdio.h>
#include <string.h>
#include <Python.h>

void print_python_bytes(PyObject *p)
{
Py_ssize_t bytsize, i;
char *str;
int x;
bytsize = PyBytes_Size(p);

printf("[.] bytes object info size: %d", (int)bytsize);

str = PyBytes_AsString(p);
if (strcmp(p->ob_type->tp_name, "bytes")) 
{
printf(" [ERROR] Invalid Bytes Object\n"); 
return; 
}

printf("   trying string: ");
for (x = 0; str[x]; x++)
printf("%s", str[x]);
printf("\n");

if (bytsize <= 10)
{
printf("   first %d bytes: ", (int)bytsize + 1);
for (i = 0; i <= bytsize; i++)
printf("%x ", (unsigned int*)str[i]);
printf("\n");
}
else
{
printf("   first 10 bytes: ");
for (i = 0; i < 10; i++)
printf("%x ", (unsigned int*)str[i]);
printf("\n");
}
}

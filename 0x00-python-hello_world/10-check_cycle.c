#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: pointer to head of list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
listint_t *new;
listint_t *ne;

if (!list)
return (0);

ne = new = list;
while (ne && new && new->next)
{
new = new->next->next;
ne = ne->next;
if (ne == new)
{
return (1);
}
}
return (0);
}

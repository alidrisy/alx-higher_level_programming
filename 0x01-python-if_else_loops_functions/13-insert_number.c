#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: a pointer to list of node
* @number: is a number of node
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *ne, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
ne = *head;

new->n = number;

if (ne == NULL || ne->n >= number)
{
new->next = ne;
*head = new;
return (new);
}

while (ne && ne->next && ne->next->n < number)
ne = ne->next;
new->next = ne->next;
ne->next = new;
return (new);
}



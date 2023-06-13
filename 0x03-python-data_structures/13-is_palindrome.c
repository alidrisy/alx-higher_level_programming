#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* len_list - get the length of a linked list
* @new: a pointer to linked list
* Return: length of linked list
*/

int len_list(listint_t *new)
{
int x = 0;

while (new != NULL)
{
new = new->next;
x++;
}
return (x);
}

/**
* is_plindrome - check if the linked list is plindrome
* @head: a pointer to linked list
* Return: 1 if yes 0 if no
*/

int is_palindrome(listint_t **head)
{
	int *node, i, x = 0, c;
	listint_t *new;

	if (*head == NULL)
	return (1);
	new = *head;
	c = len_list(new);
	node =(int *)  malloc(sizeof(int) * c);
	while (new != NULL)
	{
		node[x] = new->n;
		x++;
		new = new->next;
	}
	for (i = 0, x = c - 1; i < x; i++, x--)
	{
		if (node[i] != node[x])
		return (0);
	}
	return (1);
}

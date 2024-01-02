#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - func in C can checks if a singly linked list has
 * cycle in it
 * @list: head of linked list
 *
 * Return: 0 if there is no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (!list)
		return (0);

	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
			return (1);
	}
	return (0);
}

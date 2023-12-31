#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number int =o sorted singly linked list
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listin_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			return (new);
		}
		runner = runner->next;
	}

	new->next = NULL;
	runner->next = new;
	return (new);
}

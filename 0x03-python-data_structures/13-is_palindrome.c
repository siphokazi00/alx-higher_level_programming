#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;

	if (*head == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev_slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = reverse_list(slow);
	slow = *head;

	while (second_half != NULL)
	{
		if (second_half->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		second_half = second_half->next;
		slow = slow->next;
	}

	prev_slow->next = reverse_list(prev_slow->next);

	return (is_palindrome);
}

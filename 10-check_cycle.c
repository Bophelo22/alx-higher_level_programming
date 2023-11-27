#include "lists.h"
/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it.
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *slowList, *fastList;
slowList = list;
fastList = list;

if (list)
{
slowList = slowList->next;
fastList = fastList->next->next;
if (slowList == fastList)
{
return (1);
}
return (0);
}
else
{
return (0);
}
}

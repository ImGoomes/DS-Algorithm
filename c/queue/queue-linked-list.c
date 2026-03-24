#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
  int value;
  struct Node *next;
} Node;

Node *node_new(int value){
  Node *node = (Node *)malloc(sizeof(Node));
  node->value = value;
  node->next = NULL;
  return node;
}

typedef struct{
  struct Node *head;
  struct Node *tail;
} LinkedList;

LinkedList *linked_list_new(){
  LinkedList *ll = (LinkedList *)malloc(sizeof(LinkedList));
  ll->head = NULL;
  ll->tail = NULL;
  return ll;
}

void enqueue(LinkedList *ll, int value){
  Node *node = node_new(value);

  if(!ll->head){
    ll->head = node;
    ll->tail = node;
    return;
  }

  ll->tail->next = node;
  ll->tail = ll->tail->next;
}

void dequeue(LinkedList *ll, int value){

}

bool empty(LinkedList *ll){
  if(!ll->head){
    return true;
  }

  return false;
}

void print(LinkedList *ll){
  Node *pointer = ll->head;
  while(pointer){
    printf("%d -> ", pointer->value);
    pointer = pointer->next;
  }
  printf("NULL\n");
}

int main(){
 LinkedList *ll = linked_list_new();

  // enqueue
  enqueue(ll, 5);
  enqueue(ll, 4);
  enqueue(ll, 7);
  enqueue(ll, 9);
  printf("Initial enqueue: ");
  print(ll);

  // dequeue
  //push_front(ll);
  printf("After dequeue: ");
  print(ll);

  // empty
  //pop_front(ll);
  printf("After dequeue all: ");
  print(ll);
  printf("%b, is empty", empty(ll));

  return 0;
}

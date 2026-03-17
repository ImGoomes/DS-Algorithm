#include <stdio.h>
#include <stdlib.h>

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
} LinkedList;

LinkedList *linked_list_new(){
  LinkedList *ll = (LinkedList *)malloc(sizeof(LinkedList));
  ll->head = NULL;
  return ll;
}

int size(LinkedList *ll){
  int count = 0;
  if (ll->head == NULL){
    return count;
  }

  Node *pointer = ll->head;

  while (pointer){
    count++;
    pointer = pointer->next;
  }
  return count;
}

int main(){

}

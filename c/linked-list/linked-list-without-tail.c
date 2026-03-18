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
} LinkedList;

LinkedList *linked_list_new(){
  LinkedList *ll = (LinkedList *)malloc(sizeof(LinkedList));
  ll->head = NULL;
  return ll;
}

int size(LinkedList *ll){
  int count = 0;
  Node *pointer = ll->head;

  while (pointer){
    count++;
    pointer = pointer->next;
  }
  return count;
}

bool is_empty(LinkedList *ll){
  if (ll->head){
    return false;
  }

  return true;
}

int value_at(LinkedList *ll, int index){
  int count = 0;
  Node *pointer = ll->head;

  while (pointer){
    if(count == index){
      return pointer->value;
    }

    count++;
    pointer = pointer->next;
  }

  return -1;
}

void push_front(LinkedList *ll, int value){
  Node *pointer = ll->head;
  Node *node = node_new(value);

  ll->head = node;
  node->next = pointer;
}

void pop_front(LinkedList *ll){
  Node *old_head = ll->head;

  if(ll->head){
    ll->head = ll->head->next;
    free(old_head);
  }
}

void push_back(LinkedList *ll, int value){
  Node *pointer = ll->head;
  Node *node = node_new(value);

  if(!pointer){
    ll->head = node;
    return;
  }

  while (pointer){
    if(!pointer->next){
      pointer->next = node;
      break;
    }
    pointer = pointer->next;
  }
}


int main(){

}

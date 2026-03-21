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
  Node *pointer = ll->head;
  int counter = 0;

  while (pointer){
    counter++;
    pointer = pointer->next;
  }
  return counter;
}

bool is_empty(LinkedList *ll){
  if (ll->head){
    return false;
  }

  return true;
}

int value_at(LinkedList *ll, int index){
  Node *pointer = ll->head;
  int counter = 0;


  while (pointer){
    if(counter == index){
      return pointer->value;
    }

    counter++;
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

void pop_back(LinkedList *ll){
  Node *pointer = ll->head;
  Node *prev_node = ll->head;

  while (pointer){
    if(!pointer->next){
      if(pointer == prev_node){
        ll->head = NULL;
      }
      prev_node->next = NULL;
      free(pointer);
      break;
    }
    prev_node = pointer;
    pointer = pointer->next;
  }
}

int front(LinkedList *ll){
  if(ll->head){
    return ll->head->value;
  }

  exit(1);
}

int back(LinkedList *ll){
  Node *pointer = ll->head;
  while(pointer){
    if(!pointer->next){
      return pointer->value;
    }
    pointer = pointer->next;
  }

  exit(1);
}

void insert_at(LinkedList *ll, int value, int index){
  Node *pointer = ll->head;
  Node *prev_node = ll->head;
  Node *node = node_new(value);
  int counter = 0;

  // Empty list
  if(!pointer){
    if(index > 0){
      printf("Index out of bounds");
      return;
    }
    ll->head = node;
  }

  while(pointer) {
    if(counter == index){
      if(index == 0){
        ll->head = node;
        node->next = pointer;
        return;
      }
      prev_node->next = node;
      node->next = pointer;
      return;
    }

    if(!pointer->next){
      printf("Index out of bounds");
      return;
    }

    prev_node = pointer;
    pointer = pointer->next;
    counter++;
  }
}

void remove_at(LinkedList *ll, int index){
  Node *pointer = ll->head;
  Node *prev_node = ll->head;
  int counter = 0;
 
  // Empty list
  if(!pointer){
    printf("Index out of bounds");
    return;
  }

  while(pointer){
    if(counter == index){
      if(index == 0){
        ll->head = pointer->next;
        free(pointer);
        return;
      }

      prev_node->next = pointer->next;
      free(pointer);
      return;
    }

    prev_node = pointer;
    pointer = pointer->next;
    counter++;
  }
}

int value_n_from_end(LinkedList *ll, int n){
  int value = size(ll) - n;
  int index = value_at(ll, value);

  return index;
}

void reverse(LinkedList *ll){
  Node *pointer = ll->head;
  Node *next = ll->head;
  Node *prev_node = NULL;


  if (is_empty(ll)){
    printf("The linked list is empty");
    return;
  }

  while(pointer){
    next = pointer->next;
    pointer->next = prev_node;
    prev_node = pointer;
    pointer = next;
  }

  ll->head = prev_node;
}

void remove_value(LinkedList *ll, int value){
  Node *pointer = ll->head;
  int counter = 0;

  if (is_empty(ll)){
    printf("The linked list is empty");
    return;
  }

  while(pointer){
    if(pointer->value == value){
      remove_at(ll, counter);
      return;
    }

    pointer = pointer->next;
    counter++;
  }
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

  // push_back
  push_back(ll, 1);
  push_back(ll, 2);
  push_back(ll, 3);
  push_back(ll, 4);
  push_back(ll, 5);
  printf("Initial: ");
  print(ll);

  // push_front
  push_front(ll, 0);
  printf("After push_front(0): ");
  print(ll);

  // pop_front
  pop_front(ll);
  printf("After pop_front: ");
  print(ll);

  // pop_back
  pop_back(ll);
  printf("After pop_back: ");
  print(ll);

  // size
  printf("Size: %d\n", size(ll));

  // value_at
  printf("value_at(2): %d\n", value_at(ll, 2));

  // front and back
  printf("front: %d\n", front(ll));
  printf("back: %d\n", back(ll));

  // insert_at
  insert_at(ll, 99, 2);
  printf("After insert(99, 2): ");
  print(ll);

  // remove_at
  remove_at(ll, 2);
  printf("After remove_at(2): ");
  print(ll);

  // value_n_from_end
  printf("value_n_from_end(2): %d\n", value_n_from_end(ll, 2));

  // reverse
  reverse(ll);
  printf("After reverse: ");
  print(ll);

  // remove_value
  remove_value(ll, 3);
  printf("After remove_value(3): ");
  print(ll);

  return 0;
}

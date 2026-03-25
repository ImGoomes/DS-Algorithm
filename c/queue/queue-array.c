#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
  int *data;
  int size;
  int capacity;
  int head;
  int tail;
} Arr;


Arr *array_new(){
  Arr *a = (Arr *)malloc(sizeof(Arr));
  a->capacity = 8;
  a->data = (int *)malloc(a->capacity * sizeof(int));
  a->size = 0;
  a->head = 0;
  a->tail = 0;
  return a;
}

void enqueue(Arr *a, int value){
  
}

bool empty(Arr *a){
  if(a->size <= 0){
    return true;
  }
  return false;
}

bool full(Arr *a){
  if(a->size >= a->capacity){
    return true;
  }
  return false;
}

int main(){
  Arr *a = array_new();

  enqueue(a, 10);

  return 1;
}

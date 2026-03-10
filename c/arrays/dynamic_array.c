#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
  int *data;
  int size;
  int capacity;
} Vector;

int next_power_of_2(int n) {
  int cap = 16;

  while (cap < n){
    cap = cap * 2;
  }
  return cap;
}

Vector *vector_new(int inital_capacity){
  Vector *v = (Vector *)malloc(sizeof(Vector));
  v->capacity = next_power_of_2(inital_capacity);
  v->data = (int *)malloc(v->capacity * sizeof(int));
  v->size = 0;
  return v;
}

void resize(Vector *v){
  v->capacity = v->capacity * 2;
  v->data = (int *)realloc(v->data, v->capacity * sizeof(int));
}

int vector_size(Vector *v){
  return v->size;
}

int vector_capacity(Vector *v){
  return v->capacity;
}

int vector_at(Vector *v, int index){
  if (index < 0 || index >= v->size){
    printf("Array out of bounds\n");
    exit(1);
  }
  
  return *(v->data + index);
}

void vector_push(Vector *v, int value){
  if(v->size == v->capacity){
    resize(v);
  }

  *(v->data + v-> size) = value;
  v->size = v->size + 1;
}

void insert_at(Vector *v, int value, int index){
  int i = v->size;

  if (v->capacity == v->size){
    resize(v);
  }
 
  while (i > index) {
    *(v->data + i) = *(v->data + (i-1));
    i--;
  }
  *(v->data + i) = value;
  v->size = v->size +1;
}

void delete_at(Vector *v, int index){
  if(index >= v->size){
    printf("Array out of bounds\n");
    exit(1);
}

  while(index < v->size - 1){
    *(v->data + index) = *(v->data + (index + 1));
    index++;
  }

  v->size = v->size - 1;
}

void vector_free(Vector *v){
  free(v->data);
  free(v);
}

bool vector_is_empty(Vector *v){
  if (v->size <= 0){
    return true;
  } else {
    return false;
  }
}

int main() {
  Vector *v = vector_new(16);

  int capacity = vector_capacity(v);
  printf("capacity: %d\n", vector_capacity(v));

  printf("Is empty? %d\n", vector_is_empty(v));

  vector_push(v, 2);
  vector_push(v, 4);
  vector_push(v, 6);
  vector_push(v, 8);

  printf("Is empty? %d\n", vector_is_empty(v));

  printf("Size: %d\n", vector_size(v));
  printf("Element at 3: %d\n", vector_at(v, 3));

  insert_at(v, 0, 1);
  printf("Element at 1: %d\n", vector_at(v, 1));
  
  delete_at(v, 0);
  printf("Element at 1: %d\n", vector_at(v, 1));

  int size = vector_size(v);
  for(int i = 0; i < size; i++){
    printf("Element at %d: %d\n", i, vector_at(v, i));
  }

  vector_free(v);
  v = NULL;
}

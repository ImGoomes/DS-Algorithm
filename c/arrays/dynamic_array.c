#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *data;
  int size;
  int capacity;
} Vector;


int main() {

}

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

int vector_size(Vector *v){
  return v->size;
}

int vector_capacity(Vector *v){
  return v->capacity;
}

int vector_at(Vector *v, int i){
  if (i < 0 || i >= v->size){
    printf("Array out of bounds\n");
    exit(1);
  }
  
  return *(v->data + i);
}

void vector_push(Vector *v, int value){
  if(v->size == v->capacity){
    v->capacity = v->capacity * 2;
    v->data = (int *)realloc(v->data, v->capacity * sizeof(int));
  }

  *(v->data + v-> size) = value;
  v->size = v->size + 1;
}



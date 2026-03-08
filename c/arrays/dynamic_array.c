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

int vector_at(Vector *v, int index){
  if (index < 0 || index >= v->size){
    printf("Array out of bounds\n");
    exit(1);
  }
  
  return *(v->data + index);
}

void vector_push(Vector *v, int value){
  if(v->size == v->capacity){
    v->capacity = v->capacity * 2;
    v->data = (int *)realloc(v->data, v->capacity * sizeof(int));
  }

  *(v->data + v-> size) = value;
  v->size = v->size + 1;
}

void insert_at(Vector *v, int value, int index){
  int i = v->size;

  if (v->capacity == v->size){
    v->capacity = v->capacity * 2;
    v->data = (int *)realloc(v->data, v->capacity * sizeof(int));
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

void voctor_free(Vector *v){
  free(v->data);
  free(v);
  *v = NULL;
}

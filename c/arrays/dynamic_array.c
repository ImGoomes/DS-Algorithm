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

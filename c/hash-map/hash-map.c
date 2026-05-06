#include <stdio.h>

// Implement hash map using linear probing

enum State {
  EMPTY,
  BUSY,
  REMOVED
};

typedef struct {
  int key;
  int value;
  enum State state;
} Slot;

typedef struct {
  int size;
  Slot *slot;
} HashMap;

void add(int key, int valeu) {
  
}

int main() {

}

// hash(k, m) - k = key / m = size
// add(key, value)
// exists(key)
// get(key)
// remove(key)


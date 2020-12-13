
#include <stdbool.h>
#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <stddef.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

const unsigned long int N = 16384;      // Max # of linked-lists in hash array (power of 2)
node *table[N];                         // Initialize hash array
long int wcount;                        // Track # of words hashed into dictionary

// Returns true if word is in dictionary else false
bool check(const char *word)
{
   unsigned long int index = hash(word);                            // Hash word for access key to its LL

   for (node *tmp = table[index]; tmp != NULL; tmp = tmp->next)     // Iterate through LL, search for word (does it exist in loaded dictionary?)
   {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
   }
    return false;
}

// Hashes word to a number
unsigned long int hash(const char *word)
{
    unsigned long int hash = 0;
    unsigned int i = 0;
    unsigned int wlen = strlen(word);

    for(; i < wlen; i++)
    {
        hash = hash * 37 + tolower(word[i]);
    }


    hash = hash % N;                // Keep hash key in-bounds

    return hash;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    unsigned long int index = 0;
    char word[LENGTH];

    FILE* pfile = fopen(dictionary, "r");       // Open dictionary file
    if (pfile == NULL)
        return false;



    while (fscanf(pfile, "%s", word) != EOF)    // Scan file, write word into buffer
    {
        node *n = malloc(sizeof(node));         // malloc space for & declare node
        if (n == NULL)
            return false;

        for (int i = 0; i < strlen(word); i++)
        {
            if (isalpha(word[i]))
                word[i] = tolower(word[i]);
        }

        strcpy(n->word, word);                  // Populate node
        n->next = NULL;

        index = hash(n->word);                  // Get the word's hash value
        wcount ++;                              // Update count of words loaded into dictionary

        n->next = table[index];                 // Colonize linked list @ hash value of array
        table[index] = n;
    }
    return true;
}

// Returns number of words in dictionary if loaded else 0
unsigned long int size(void)
{
    return wcount;
}

// Unloads dictionary from memory
bool unload(void)
{
    for (unsigned long int i = 0; i < N; i ++)      // Iterate thru hash table
    {
        if (table[i] != NULL)                       // Check if LL in location
        {
            node *tmp = table[i];                   // Temporary pointer
            if (table[i]->next != NULL)             // Check LL length > 1
            {
                node *crsr = table[i]->next;        // Temporary pointer #2 (for LL length > 1)
                while(true)
                {
                    free(tmp);                      // Free pointee
                    if(crsr->next == NULL)              // Check if EOL,
                    {
                        free(crsr);                     // Free node's at EOL, exit function
                        break;
                    }
                    tmp = crsr;                     // Move down list
                    crsr = crsr->next;              // Move down list
                }
            }
            else
                free(tmp);                          // Free pointee, case: (LL length == 1)
        }
    }
    //success
    return true;
}

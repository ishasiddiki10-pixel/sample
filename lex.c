#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isKeyword(char *s)
{
    char *kw[] = {"int","float","char","if","else",
                  "while","for","return","void"};
    int i;

    for(i = 0; i < 9; i++)
        if(strcmp(s, kw[i]) == 0)
            return 1;

    return 0;
}

void lex(char *s)
{
    int i = 0, j, k, n = strlen(s);
    char b[100], c;
    char *ops[] = {"==","!=","<=",">=","++","--","&&","||"};

    while(i < n)
    {
        c = s[i];

        if(isspace(c))
            i++;

        else if(s[i] == '/' && s[i+1] == '/')
        {
            while(i < n && s[i] != '\n')
                i++;
        }

        else if(s[i] == '/' && s[i+1] == '*')
        {
            char *p = strstr(s+i+2, "*/");
            i = p ? p-s+2 : n;
        }

        else if(isalpha(c) || c == '_')
        {
            j = 0;

            while(isalnum(s[i]) || s[i] == '_')
                b[j++] = s[i++];

            b[j] = '\0';

            if(j > 20)
                printf("Invalid Identifier: %s\n", b);
            else
                printf("%s: %s\n",
                       isKeyword(b) ? "Keyword" : "Identifier", b);
        }

        else if(isdigit(c))
        {
            j = 0;

            while(isdigit(s[i]))
                b[j++] = s[i++];

            if(s[i] == '.' && isdigit(s[i+1]))
            {
                b[j++] = s[i++];

                while(isdigit(s[i]))
                    b[j++] = s[i++];
            }

            b[j] = '\0';
            printf("Number: %s\n", b);
        }

        else
        {
            int found = 0;

            for(k = 0; k < 8; k++)
            {
                if(strncmp(s+i, ops[k], 2) == 0)
                {
                    printf("Operator: %s\n", ops[k]);
                    i += 2;
                    found = 1;
                    break;
                }
            }

            if(found)
                continue;

            if(strchr("+-*/%=<>!", c))
                printf("Operator: %c\n", c);
            else if(strchr("(){}[];,", c))
                printf("Symbol: %c\n", c);
            else
                printf("Unknown: %c\n", c);

            i++;
        }
    }
}

int main()
{
    char s[10000];
    FILE *f = fopen("input.txt", "r");

    if(f == NULL)
    {
        printf("File not found");
        return 1;
    }

    fread(s, 1, sizeof(s)-1, f);
    fclose(f);

    s[sizeof(s)-1] = '\0';
    lex(s);

    return 0;
}
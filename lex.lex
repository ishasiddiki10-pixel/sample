%{
#include <stdio.h>
%}

%option noyywrap

KEYWORD (int|float|char|if|else|while|for|return|void)
ID [a-zA-Z_][a-zA-Z0-9_]*
NUMBER [0-9]+(\.[0-9]+)?

%%

[ \t\n]+          ;

"//".*            ;

"/*"([^*]|\*+[^*/])*\*+"/"   ;

{KEYWORD}         { printf("Keyword: %s\n", yytext); }

{NUMBER}          { printf("Number: %s\n", yytext); }

{ID}              { printf("Identifier: %s\n", yytext); }

"=="|"!="|"<="|">="|"++"|"--"|"&&"|"||"
                  { printf("Operator: %s\n", yytext); }

[+\-*/%=<>!]      { printf("Operator: %s\n", yytext); }

[(){}[\];,]       { printf("Symbol: %s\n", yytext); }

.                 { printf("Unknown: %s\n", yytext); }

%%

int main()
{
    printf("Enter source code (Ctrl+Z to stop):\n");
    yylex();
    return 0;
}
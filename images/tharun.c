#inciude<stdio.h>
int main()
{
    int n,fact=1,i;
    printf("Enter a number:");
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        fact=fact*i;
    }
    printf("the fact of %d is=%d",nfact);
    return 0;
}

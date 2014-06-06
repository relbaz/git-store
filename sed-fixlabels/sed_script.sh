sed -r '
s/^(Business)(\W+)/LBL1\2/
t skip

s/^(X1)(\W+)/LBL2\2/
t skip

s/^(\w+)(\W+)/DEFAULT\2/
:skip
'

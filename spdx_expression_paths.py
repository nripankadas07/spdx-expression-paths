"""Enumerate bounded syntactic choices in SPDX-style license expressions."""
import argparse,json,re,sys

def choices(expression,limit=128):
    if not isinstance(expression,str) or not expression.strip() or len(expression)>4096: raise ValueError('expression must be 1..4096 characters')
    if type(limit) is not int or not 1<=limit<=1024: raise ValueError('limit must be 1..1024')
    tokens=[];pos=0
    for m in re.finditer(r'\s*([A-Za-z0-9][A-Za-z0-9.+:-]*|[()])',expression):
        if m.start()!=pos: raise ValueError('invalid token')
        tokens.append(m.group(1));pos=m.end()
    if expression[pos:].strip() or len(tokens)>256: raise ValueError('invalid token or more than 256 tokens')
    i=0
    def unique(paths):
        # Dedupe paths, without removing stricter conjunctions or imposing policy.
        u=sorted({tuple(sorted(set(p))) for p in paths})
        if len(u)>limit: raise ValueError('alternative limit exceeded')
        return u
    def atom(depth):
        nonlocal i
        if depth>32 or i>=len(tokens): raise ValueError('missing operand or nesting exceeds 32')
        t=tokens[i];i+=1
        if t=='(':
            a=expr(depth+1)
            if i>=len(tokens) or tokens[i]!=')': raise ValueError('missing closing parenthesis')
            i+=1;return a
        if t in ('AND','OR','WITH',')'): raise ValueError('identifier required')
        if i<len(tokens) and tokens[i]=='WITH':
            i+=1
            if i>=len(tokens) or tokens[i] in ('AND','OR','WITH','(',')'): raise ValueError('exception identifier required')
            t+=' WITH '+tokens[i];i+=1
        return [(t,)]
    def conjunction(depth):
        nonlocal i
        a=atom(depth)
        while i<len(tokens) and tokens[i]=='AND':
            i+=1;b=atom(depth)
            if len(a)*len(b)>4096: raise ValueError('expansion work limit exceeded')
            a=unique([x+y for x in a for y in b])
        return a
    def expr(depth):
        nonlocal i
        a=conjunction(depth)
        while i<len(tokens) and tokens[i]=='OR':
            i+=1;a=unique(a+conjunction(depth))
        return a
    result=unique(expr(0))
    if i!=len(tokens): raise ValueError('unexpected token')
    return {'alternatives':[list(p) for p in result],'count':len(result),'scope':'syntax only; identifiers are not registry-validated; no legal/compliance decision'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('expression');p.add_argument('--limit',type=int,default=128);a=p.parse_args()
    try: print(json.dumps(choices(a.expression,a.limit),sort_keys=True));return 0
    except ValueError as e: print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':sys.exit(main())

def f(value,seq = []):
    seq.append(value)
    return seq

print(f(3))
print(f(10))
# ====
"""đù tại sao nó lại nối vào vậy, tránh việc sử dụng 
avoiding mutable optional arguments
đối số tuỳ chọn có thể thay đổi"""

def f(value,seq = None):
    if not seq:
        seq =[]
    seq.append(value)
    return seq
print(f(3))
print(f(10))

"""
Nói chung chưa giải thích kĩ được vì python nó quá co dãn
"""


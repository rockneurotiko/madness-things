function is_divisible(n::Int64, i::Int64)
    return n%i == 0
end


function is_prime(n::Int64)
    if n <= 3
        return true
    end
    if is_divisible(n,2)
        return false
    end
    i = 3
    while i <= sqrt(n)
        if is_divisible(n,i)
            return false
        end
        i+=2
    end

    return true

end


println(is_prime(100))

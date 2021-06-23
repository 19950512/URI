main = do 
    a <- getLine
    b <- getLine

    let aa = read a :: Integer
    let bb = read b :: Integer
    let x = aa + bb
    putStrLn("X = " ++ show x)
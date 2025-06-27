F play_random(n)
   V pardoned = 0
   V in_drawer = Array(0.<100)
   V sampler = Array(0.<100)
   L 0 .< n
      random:shuffle(&in_drawer)
      V found = 0B
      L(prisoner) 100
         found = 0B
         L(reveal) random:sample(sampler, 50)
            V card = in_drawer[reveal]
            I card == prisoner
               found = 1B
               L.break
         I !found
            L.break
      I found
         pardoned++
   R Float(pardoned) / n * 100

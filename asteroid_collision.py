def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            alive = True
            # collision only possible when current asteroid is moving left and stack top moving right
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    # right-moving asteroid explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    # both explode
                    stack.pop()
                    alive = False
                    break
                else:
                    # current left-moving asteroid explodes
                    alive = False
                    break
            if alive:
                stack.append(a)
        return stack

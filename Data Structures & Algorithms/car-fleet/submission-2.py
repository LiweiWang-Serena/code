class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse=True)
        st = []
        for position, speed in cars:
            time = (target - position) / speed
            if not st or time > st[-1]:
                st.append(time)
        return len(st)

        
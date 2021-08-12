## Sorting Algorithm Keywords
- Runtime : 얼마나 빠르게 연산이 되는지 (O(n), O(nlog(n)), O(n^2) 등)
- Stable sort : 여러번 정렬했을 때 얼마나 일관되는 결과를 반환하는지
(문자 순서로 정렬 후 가격 순서로 정렬하면 같은 가격인 경우 문자대로 정렬이 되어 있는지 등)
- In-place sort : 입력되는 값에 할당되는 메모리 공간 이외에 추가적으로 메모리가 필요한지
- Pathological case : A case in which the input data is specifically designed to make your algorithm run as slowly as possible

## sorting이 필요한 이유
- 데이터를 검색하는데 훨씬 빠르다.
- 데이터를 선택하는데 쉬워진다. --> n번째로 큰 수
- 중복된 데이터를 찾는데 빠르다.
- 분석적인 측면에서 빈도수를 찾는데 빠르다.

## Time Complexity 시간 복잡도
상수 --> log(n) --> n --> nlog(n) --> n^2 --> 상수^n --> n!


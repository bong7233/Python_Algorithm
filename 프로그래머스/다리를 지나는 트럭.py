def solution(bridge_length, weight, truck_weights):
    count = 0          # 경과 시간
    weight_sum = 0     # 다리위의 트럭들의 무게의 함
    bridge = []        # 다리위에 있는 트럭들

    while truck_weights:
        count += 1

        # 트럭이 다리위로 올라갈 수 있는 조건
        # (다리위에 올라갈 수 있는 한도랑 같아도 뒤에서 하나씩 빼주기 때문에 상관없다)
        if ((weight_sum + truck_weights[0]) <= weight and len(bridge) <= bridge_length):
            bridge.append(truck_weights.pop(0)) # 트럭을 다리위에 올리고
            weight_sum += bridge[-1] # 올린 트럭의 무게를 총 무게에 더한다
        else:
            # 다리위로 올라갈 수 없다면 빈 공간으로 채운다
            # (bridge.pop(0)을 했을 때 경과 시간이 지나지도 않았는데 다리에 들어오자마자 나가는걸 막기 위해)
            bridge.append(0)

        # 경과한 시간이 다리 길이보다 크면, 다리에서 나온 트럭들의 무게를 빼준다
        # (배열의 크기가 다리의 길이만큼 되도록 기다림, 첫 트럭 빠져나올 때 까지 기다리는 코드)
        if count >= bridge_length:
            weight_sum -= bridge.pop(0)

    # 총 경과 시간 + 다리위에 있는 트럭들이 지나가는데 소요 할 시간
    return count + bridge_length
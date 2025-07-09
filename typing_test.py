import time

def typing_speed_test():
    print("타자 속도 테스트를 시작합니다!")
    print("아래 문장을 입력하세요:")
    test_sentence = "이것은 타자 속도 테스트 문장입니다. 정확히 입력해주세요."
    print(f"\n{test_sentence}\n")

    input("준비가 되면 Enter 키를 누르세요...")
    start_time = time.time()
    
    user_input = input("\n>> ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = correct_chars / len(test_sentence) * 100
    speed = len(user_input) / elapsed_time * 60  # 분당 타수 (CPM)

    print("\n=== 결과 ===")
    print(f"입력 시간: {elapsed_time:.2f}초")
    print(f"정확도: {accuracy:.2f}%")
    print(f"분당 타수: {speed:.2f} 타/분")

if __name__ == "__main__":
    typing_speed_test()

/*
문제 설명
여러 개의 로그 문자열이 배열 logs로 주어집니다.
정상적인 로그는 반드시 아래 순서와 형식을 따라야 합니다.
team_name : 값 application_name : 값 error : 값 message : 값
각 로그는 총 4개의 항목으로 구성됩니다.
각 항목은 다음과 같은 형태를 가집니다.
항목이름 : 값
항목 사이와 : 앞뒤에는 공백이 정확히 한 칸 존재한다고 가정합니다.
각 항목의 값은 공백을 포함하지 않으며, 영문 대문자, 영문 소문자, _로 구성될 수 있습니다.
정상적인 형식을 만족하지 않는 로그의 개수를 반환하세요.
1. 각 항목에는 값이 반드시 하나씩 존재해야 합니다.
2. 값에는 공백이 포함될 수 없습니다.
3. 값은 영문 대문자, 영문 소문자, _만 사용할 수 있습니다.

입력
[
  "team_name : alpha_team application_name : my_app error : network_error message : try_again",
  "team_name : beta application_name : service error : timeout message : please_retry",
  "team_name : gamma application_name : app error : network message : I DONT KONW"
];
출력:
1
*/

function solution(logs) {
    const pattern = /^team_name : [A-Za-z_]+ application_name : [A-Za-z_]+ error : [A-Za-z_]+ message : [A-Za-z_]+$/;

    let invalidCount = 0;

    for (const log of logs) {
        if (!pattern.test(log)) {
            invalidCount++;
        }
    }

    return invalidCount;
}

/*
/^team_name : [A-Za-z_]+ application_name : [A-Za-z_]+ error : [A-Za-z_]+ message : [A-Za-z_]+$/;

[A-Za-z_]
    -> A-Z, a-z, _ 중 하나
+
    -> 바로 앞 조건이 1개 이상 있어야 한다는 뜻

*/
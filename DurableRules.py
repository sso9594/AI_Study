from durable.lang import *

# 규칙셋을 정의합니다.
with ruleset('medical_diagnosis'):

    # 증상: 발열이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'fever'))
    def check_fever(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'common_cold'})

    # 증상: 두통이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'headache'))
    def check_headache(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'migraine'})

    # 증상: 구토가 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'vomiting'))
    def check_vomiting(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'food_poisoning'})

    # 증상: 설사가 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'diarrhea'))
    def check_diarrhea(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'gastroenteritis'})

    # 증상: 기침이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'cough'))
    def check_cough(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'bronchitis'})

    # 증상: 가슴 통증이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'chest_pain'))
    def check_chest_pain(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'angina'})

    # 증상: 기침과 가래가 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'cough') & (m.predicate == 'has') & (m.object == 'phlegm'))
    def check_cough_with_phlegm(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'pneumonia'})

    # 증상: 두통, 설사, 구토가 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'headache') &
              (m.predicate == 'has') & (m.object == 'diarrhea') &
              (m.predicate == 'has') & (m.object == 'vomiting'))
    def check_severe_symptoms(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'food_poisoning'})

    # 증상: 흉통, 호흡 곤란이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'chest_pain') &
              (m.predicate == 'has') & (m.object == 'shortness_of_breath'))
    def check_severe_chest_pain(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'heart_attack'})

    # 증상: 가슴 통증, 심한 두통이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'chest_pain') &
              (m.predicate == 'has') & (m.object == 'severe_headache'))
    def check_severe_chest_pain_with_headache(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'migraine'})

    # 증상: 의식 잃음이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'loss_of_consciousness'))
    def check_loss_of_consciousness(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'syncope'})

    # 증상: 열이 있고 가래가 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'fever') &
              (m.predicate == 'has') & (m.object == 'phlegm'))
    def check_fever_with_phlegm(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'respiratory_infection'})

    # 증상: 열이 있고 기침이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'fever') &
              (m.predicate == 'has') & (m.object == 'cough'))
    def check_fever_with_cough(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'influenza'})

    # 증상: 심장 부전이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'heart_failure'))
    def check_heart_failure(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'congestive_heart_failure'})

    # 증상: 복통이 있을 때
    @when_all((m.predicate == 'has') & (m.object == 'abdominal_pain'))
    def check_abdominal_pain(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'diagnosis', 'object': 'gastritis'})
    
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


# 증상과 관련된 사실들을 추가합니다.
assert_fact('medical_diagnosis', {'subject': 'patient1', 'predicate': 'has', 'object': 'fever'})
assert_fact('medical_diagnosis', {'subject': 'patient2', 'predicate': 'has', 'object': 'headache'})
assert_fact('medical_diagnosis', {'subject': 'patient3', 'predicate': 'has', 'object': 'vomiting'})
assert_fact('medical_diagnosis', {'subject': 'patient4', 'predicate': 'has', 'object': 'diarrhea'})
assert_fact('medical_diagnosis', {'subject': 'patient5', 'predicate': 'has', 'object': 'cough'})
assert_fact('medical_diagnosis', {'subject': 'patient6', 'predicate': 'has', 'object': 'chest_pain'})
assert_fact('medical_diagnosis', {'subject': 'patient7', 'predicate': 'has', 'object': 'headache'})
assert_fact('medical_diagnosis', {'subject': 'patient7', 'predicate': 'has', 'object': 'diarrhea'})
assert_fact('medical_diagnosis', {'subject': 'patient7', 'predicate': 'has', 'object': 'vomiting'})
assert_fact('medical_diagnosis', {'subject': 'patient8', 'predicate': 'has', 'object': 'chest_pain'})
assert_fact('medical_diagnosis', {'subject': 'patient8', 'predicate': 'has', 'object': 'shortness_of_breath'})
assert_fact('medical_diagnosis', {'subject': 'patient9', 'predicate': 'has', 'object': 'chest_pain'})
assert_fact('medical_diagnosis', {'subject': 'patient9', 'predicate': 'has', 'object': 'severe_headache'})
assert_fact('medical_diagnosis', {'subject': 'patient10', 'predicate': 'has', 'object': 'loss_of_consciousness'})
assert_fact('medical_diagnosis', {'subject': 'patient11', 'predicate': 'has', 'object': 'fever'})
assert_fact('medical_diagnosis', {'subject': 'patient11', 'predicate': 'has', 'object': 'phlegm'})

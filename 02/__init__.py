from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple
from re import compile
import sys


RE_LEAST = compile(".+?(?=-)")
RE_MOST = compile("-([^ ]*)")
RE_CHAR = compile("[a-zA-Z]")


class PolicyType(Enum):
    ONE, TWO = 1, 2


@dataclass
class PasswordPolicy:
    policy_type: PolicyType
    validated_char: str
    validation_option1: int
    validation_option2: int

    def validate(self, password: str) -> bool:
        if self.policy_type == PolicyType.ONE:
            return self._validate_type_one(password)
        elif self.policy_type == PolicyType.TWO:
            return self._validate_type_two(password)

    def _validate_type_one(self, password: str) -> bool:
        occurances = 0
        for char in password:
            if char == self.validated_char:
                occurances += 1
        return self.validation_option1 <= occurances <= self.validation_option2

    def _validate_type_two(self, password: str) -> bool:
        checked_char1 = password[self.validation_option1 - 1]
        checked_char2 = password[self.validation_option2 - 1]
        return (checked_char1 == self.validated_char) ^ (checked_char2 == self.validated_char)


def read_input() -> List[str]:
    with open("input.txt", "r") as file:
        return [e.strip("\n") for e in list(file)]


def get_policy_type() -> PolicyType:
    if len(sys.argv) == 2:
        if sys.argv[1] == "--part-two":
            return PolicyType.TWO

    return PolicyType.ONE


def read_policy_and_password(line: str, _type: PolicyType) -> Tuple[PasswordPolicy, str]:
    policy_str, password = line.split(":")

    policy_arg1 = int(RE_LEAST.search(policy_str).group(0))
    policy_arg2 = int(RE_MOST.search(policy_str).group(1))
    policy_char = RE_CHAR.search(policy_str).group(0)

    return (PasswordPolicy(_type, policy_char, policy_arg1, policy_arg2), password[1:])


def main() -> None:
    valid_count = 0
    policy_type = get_policy_type()

    lines = read_input()
    for line in lines:
        policy, password = read_policy_and_password(line, policy_type)
        if policy.validate(password):
            valid_count += 1

    print(f"result: {valid_count} valid passwords")


if __name__ == '__main__':
    main()


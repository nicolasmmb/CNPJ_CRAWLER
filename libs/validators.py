from typing import Self


class PydanticConversor:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> Self:
        return cls(v)


class CNPJ(str, PydanticConversor):
    __DIGT_01: int
    __DIGT_02: int
    __STD_01: list[int] = list(range(6, 10)) + list(range(2, 10))
    __STD_02: list[int] = list(range(5, 10)) + list(range(2, 10))

    def __new__(cls, _: str) -> Self:
        is_valid: bool = cls.__validate(cnpj=_)
        if is_valid:
            return super().__new__(cls, _)
        else:
            raise ValueError("Invalid CNPJ")

    @classmethod
    def __validate(cls, cnpj: str) -> bool:
        cnpj = cls.sanitize(cnpj=cnpj)
        cls.constraint(cnpj=cnpj)

        sum_dig: int = sum(int(cnpj[i]) * n for i, n in enumerate(cls.__STD_01))
        cls.__DIGT_01: int = sum_dig % 11

        sum_dig: int = sum(int(cnpj[i]) * n for i, n in enumerate(cls.__STD_02))
        cls.__DIGT_02: int = sum_dig % 11

        return cls.compare_digits(cnpj)

    @classmethod
    def compare_digits(cls, cnpj: str) -> bool:
        if cls.__DIGT_01 >= 10:
            cls.__DIGT_01 = 0
        if cls.__DIGT_02 >= 10:
            cls.__DIGT_02 = 0
        is_equal_digt_01: bool = cls.__DIGT_01 == int(cnpj[12])
        is_equal_digt_02: bool = cls.__DIGT_02 == int(cnpj[13])
        return all([is_equal_digt_01, is_equal_digt_02])

    @classmethod
    def constraint(cls, cnpj: str) -> None:
        if len(cnpj) < 14:
            raise ValueError("Length is less than 14")

        if len(set(cnpj)) == 1:
            raise ValueError("All characters is equal")

    @classmethod
    def sanitize(cls, cnpj: str) -> str:
        cnpj = cnpj.replace(".", "")
        cnpj = cnpj.replace("/", "")
        return cnpj.replace("-", "")

    @property
    def DIGT_01(self) -> int:
        return self.__DIGT_01

    @property
    def DIGT_02(self) -> int:
        return self.__DIGT_02

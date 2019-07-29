import itertools
from typing import Optional, Iterator

__author__ = "Bojan Potočnik"


def gmail_permutator(base_address: str, limit: Optional[int] = None, *,
                     return_only_base: bool = False) -> Iterator[str]:
    """
    Generate new Gmail addresses by permutations of dots in the address.

    :param base_address: Base Gmail address.
    :param limit: If provided, only `limit` number of addresses will be generated.
    :param return_only_base: Whether to return only the base address without the @domain.

    :raises ValueError: if the provided parameters are invalid.
    """
    if not base_address:
        raise ValueError("Base email address is mandatory")
    address, domain = base_address.split("@")  # type: str, str
    if domain not in ("gmail.com", "googlemail.com"):
        raise ValueError(f"Only Gmail hosted email addresses are supported, not '{domain}'")
    if not (address and address.isprintable() and (address.count(" ") == 0)):
        raise ValueError(f"Address '{address}' is not valid email address (RFC 5322)")

    last_part = "" if return_only_base else ("@" + domain)

    # Imagine the address as the binary number - there is a place for binary number between every char.
    # There can be less chars that the required bits to represent the number - in that case repeat the process.
    max_dots = 2 ** (len(address) - 1)

    counter = 0
    for count in itertools.count():
        # Number can already be larger than maximum number of the dots.
        dots_from_before, count_left = divmod(count, max_dots)
        if not count_left:
            continue

        counter += 1
        if (limit is not None) and (counter > limit):
            break

        dots = [dots_from_before] * (len(address) - 1)

        for bit in range(len(dots)):
            if count_left & (1 << bit):
                dots[bit] += 1

        s = address[0]
        for i, num_dots in enumerate(dots, 1):
            s += num_dots * "." + address[i]

        yield s if return_only_base else (s + last_part)

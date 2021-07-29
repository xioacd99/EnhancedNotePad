import string
import decimal
from decimal import Decimal

decimal.getcontext().prec = 100


class ArithmeticCode(object):
    def encode(self, str, N=5):
        count = dict.fromkeys(string.ascii_lowercase, 1)  # probability table
        cdf_range = dict.fromkeys(string.ascii_lowercase, 0)
        pdf = dict.fromkeys(string.ascii_lowercase, 0)

        low = 0
        high = Decimal(1) / Decimal(26)

        for key, value in sorted(cdf_range.items()):
            cdf_range[key] = [low, high]
            low = high
            high += Decimal(1) / Decimal(26)

        for key, value in sorted(pdf.items()):
            pdf[key] = Decimal(1) / Decimal(26)

        # 假设待编码字符只有 26 个英文字母
        i = 26
        lower_bound = 0
        upper_bound = 1
        u = 0

        for ch in str:
            i += 1
            u += 1
            count[ch] += 1

            curr_range = upper_bound - lower_bound
            upper_bound = lower_bound + (curr_range * cdf_range[ch][1])
            lower_bound = lower_bound + (curr_range * cdf_range[ch][0])

            # update cdf_range after N symbols have been read
            if (u == N):
                u = 0
                for key, value in sorted(pdf.items()):
                    pdf[key] = Decimal(count[key]) / Decimal(i)
                low = 0
                for key, value in sorted(cdf_range.items()):
                    high = pdf[key] + low
                    cdf_range[key] = [low, high]
                    low = high

        return lower_bound


if __name__ == '__main__':
    test = ArithmeticCode()
    ans = test.encode('helloworld')
    print(ans)

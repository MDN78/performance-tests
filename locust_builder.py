from seeds.builder import build_grpc_seeds_builder
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan
from seeds.dumps import save_seeds_result, load_seeds_result

# example of how to use builders with seeds plans

builder  = build_grpc_seeds_builder()


# Step 2. Crrate Seeds plan:
# - Create 100 users
# - Each user has:
#   - 1 account with debit card
#   - Each account has:
#       - 1 physical card

result = builder.build(
    SeedsPlan(
        users=SeedUsersPlan(
            count=100,
            credit_card_accounts=SeedAccountsPlan(
                count=1,
                physical_cards=SeedCardsPlan(count=1)
            )
        )
    )
)

print(result)

# Step 3. save result generated Seeds plan
save_seeds_result(result, scenario="seeds plan")


# Step 4. download seeds result from file
print(load_seeds_result(scenario="test-scenario"))
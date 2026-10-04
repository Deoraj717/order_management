engine = create_async_engine(
    settings.DATABASE_URL
    pool_size = 5,
    max_overflow = 10,
    pool_pre_ping = True
)

SessionLocal = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    autoflush = False,
    expire_on_commit = False
)
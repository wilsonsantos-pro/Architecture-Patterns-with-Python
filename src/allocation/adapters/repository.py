import abc
from typing import Protocol, Set

from allocation.adapters import orm
from allocation.domain import model
from repository_pattern.repository import base_repository, sqlalchemy


class IAllocationRepository:
    def get_by_batchref(self, batchref: str) -> model.Product:
        """Get product by batch reference."""


# class AbstractRepository(base_repository.AbstractRepository[model.Product]):
#    def get_by_batchref(self, batchref) -> model.Product:
#        product = self._get_by_batchref(batchref)
#        if product:
#            self.seen.add(product)
#        return product
#
#    @abc.abstractmethod
#    def _get_by_batchref(self, batchref) -> model.Product:
#        raise NotImplementedError


class SqlAlchemyRepository(sqlalchemy.AbstractSqlAlchemyRepository[model.Product]):
    def _get(self, id_):
        return self.session.query(model.Product).filter_by(sku=id_).first()

    def get_by_batchref(self, batchref):
        product = (
            self.session.query(model.Product)
            .join(model.Batch)
            .filter(
                orm.batches.c.reference == batchref,
            )
            .first()
        )
        if product:
            self.seen.add(product)
        return product
